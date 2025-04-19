#!/usr/bin/env bash
SCRIPT=${1:-src/scripts/api_request.py}
gdb -q --args  python3-dbg "$SCRIPT" <<EOF
set breakpoint pending on

# Primer breakpoint
break to_float_asm
commands
  disas
  x/12d \$rsp
  continue
end

# Segundo breakpoint
break convert_to_float
commands
  disas
  x/12d \$rsp

end

run
EOF
