# Makefile for generating an LZMA library using Emscripten.

O = .
OBJECTS = \
  $(O)/Alloc.o \
  $(O)/LzFind.o \
  $(O)/LzmaDec.o \
  $(O)/LzmaEnc.o

all: lzma.a

%.o: %.c
	$(CC) $(CFLAGS) -I. $< -o $@ -O1 -c -g -ffunction-sections

lzma.a: $(OBJECTS)
	$(AR) rv $@ $(OBJECTS)

clean:
	rm lzma.a

