/**
 * @license
 * Copyright 2019 The Emscripten Authors
 * SPDX-License-Identifier: MIT
 */

class WasmSourceMap {
  mapping = {};
  offsets = [];

  constructor(sourceMap) {
    this.version = sourceMap.version;
    this.sources = sourceMap.sources;
    this.names = sourceMap.names;

    var vlqMap = {};
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='.split('').forEach((c, i) => vlqMap[c] = i);

    // based on https://github.com/Rich-Harris/vlq/blob/master/src/vlq.ts
    function decodeVLQ(string) {
      var result = [];
      var shift = 0;
      var value = 0;

      for (var ch of string) {
        var integer = vlqMap[ch];
        if (integer === undefined) {
          throw new Error(`Invalid character (${ch})`);
        }

        value += (integer & 31) << shift;

        if (integer & 32) {
          shift += 5;
        } else {
          var negate = value & 1;
          value >>= 1;
          result.push(negate ? -value : value);
          value = shift = 0;
        }
      }
      return result;
    }

    var offset = 0, src = 0, line = 1, col = 1, name = 0;
    sourceMap.mappings.split(',').forEach(function (segment, index) {
      if (!segment) return;
      var data = decodeVLQ(segment);
      var info = {};

      offset += data[0];
      if (data.length >= 2) info.source = src += data[1];
      if (data.length >= 3) info.line = line += data[2];
      if (data.length >= 4) info.column = col += data[3];
      if (data.length >= 5) info.name = name += data[4];
      this.mapping[offset] = info;
      this.offsets.push(offset);
    }, this);
    this.offsets.sort((a, b) => a - b);
  }

  lookup(offset) {
    var normalized = this.normalizeOffset(offset);
#if USE_OFFSET_CONVERTER
    if (!wasmOffsetConverter.isSameFunc(offset, normalized)) {
      return null;
    }
#endif
    var info = this.mapping[normalized];
    if (!info) {
      return null;
    }
    return {
      file: this.sources[info.source],
      line: info.line,
      column: info.column,
      name: this.names[info.name],
    };
  }

  normalizeOffset(offset) {
    var lo = 0;
    var hi = this.offsets.length;
    var mid;

    while (lo < hi) {
      mid = Math.floor((lo + hi) / 2);
      if (this.offsets[mid] > offset) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }
    return this.offsets[lo - 1];
  }
}

var wasmSourceMapFile = '{{{ WASM_BINARY_FILE }}}.map';
wasmSourceMapFile = locateFile(wasmSourceMapFile);

function getSourceMap() {
  var buf = readBinary(wasmSourceMapFile);
  return JSON.parse(UTF8ArrayToString(buf));
}

async function getSourceMapAsync() {
  if (ENVIRONMENT_IS_WEB || ENVIRONMENT_IS_WORKER) {
    try {
      var response = await fetch(wasmSourceMapFile, {{{ makeModuleReceiveExpr('fetchSettings', "{ credentials: 'same-origin' }") }}});
      return response.json();
    } catch {
      // Fall back to getSourceMap below
    }
  }
  return getSourceMap();
}
