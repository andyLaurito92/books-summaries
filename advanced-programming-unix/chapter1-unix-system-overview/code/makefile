TARGET = myls

OBJS = myls.o apue.o

CC = cc
CFLAGS = -Wall -Wextra -O2

$(TARGET): $(OBJS)
	$(CC) $(OBJS) -o $(TARGET)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Clean

.PHONY: clean
clean:
	rm -rf $(TARGET) *o
