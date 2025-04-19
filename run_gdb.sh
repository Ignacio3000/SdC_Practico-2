#!/usr/bin/env bash
SCRIPT=${1:-src/scripts/api_c_asm.py}
gdb -q --args  python3-dbg "$SCRIPT" <<EOF
set breakpoint pending on

# Primer breakpoint
break float_to_int_asm
commands
  disas
  x/16gx \$rsp
  continue
end

# Segundo breakpoint
break to_int_asm 
commands
  disas
  x/16gx \$rsp
end

run
quit
EOF

