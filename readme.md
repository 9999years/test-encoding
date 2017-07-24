Use `./test-encoding.py -r` to print raw bytes `0x00` through `0xff` to STDOUT.
Can be piped to, e.g., `lpr -l` to inspect the codepage of an external device.

    $ ./test-encoding.py

      0123456789abcdef
      ----------------
    0  ☺☻♥♦♣
    ♫☼ 0
    1 ►◄↕‼¶§■↨↑↓→←∟↔▲▼ 1
    2  !"#$%&'()*+,-./ 2
    3 0123456789:;<=>? 3
    4 @ABCDEFGHIJKLMNO 4
    5 PQRSTUVWXYZ[\]^_ 5
    6 `abcdefghijklmno 6
    7 pqrstuvwxyz{|}~ 7
    8  8
    9  9
    a  ¡¢£¤¥¦§¨©ª«¬­®¯ a
    b °±²³´µ¶·¸¹º»¼½¾¿ b
    c ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏ c
    d ÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞß d
    e àáâãäåæçèéêëìíîï e
      ----------------
      0123456789abcdef
