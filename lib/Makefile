CC=gcc

FULL_NATIVE_NEON_HAL_OBJS=ikamatcher2_neon_hal.o ikamatcher2_neon_wrap_new.o ikamatcher2_kernel_hal.o
SEMI_NATIVE_NEON_HAL_OBJS=ikamatcher2_neon_hal.o ikamatcher2_neon_wrap.o
PY_INC=`python3 -c "import sysconfig; print(sysconfig.get_path('include'))"`
INCLUDE_DIR=-I. -I$(PY_INC)

# https://gcc.gnu.org/onlinedocs/gcc/ARM-Options.html
CPU=-mtune=cortex-a7 -mfpu=neon
CFLAGS=-std=c11 -O2 -MD

all: ikamatcher2_kernel_hal.so ikamatcher2_neon_hal.so

ikamatcher2_kernel_hal.so: $(FULL_NATIVE_NEON_HAL_OBJS)
	$(CC) $(CFLAGS) $(CPU) -fPIC $(INCLUDE_DIR) --shared -o $@ $^

ikamatcher2_neon_hal.so: $(SEMI_NATIVE_NEON_HAL_OBJS)
	$(CC) $(CFLAGS) $(CPU) -fPIC $(INCLUDE_DIR) --shared -o $@ $^

.c.o:
	$(CC) $(CFLAGS) $(CPU) -fPIC $(INCLUDE_DIR) -c $<

clean:
	-rm $(FULL_NATIVE_NEON_HAL_OBJS)
	-rm $(SEMI_NATIVE_NEON_HAL_OBJS)
	-rm ikamatcher2_kernel_hal.so ikamatcher2_neon_hal.so
	-rm $(FULL_NATIVE_NEON_HAL_OBJS:.o=.d)
	-rm $(SEMI_NATIVE_NEON_HAL_OBJS:.o=.d)

DEPS = $(FULL_NATIVE_NEON_HAL_OBJS:.o=.d) $(SEMI_NATIVE_NEON_HAL_OBJS:.o=.d)
-include $(DEPS)
