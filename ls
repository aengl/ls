#!/bin/bash

action=$1
flag=$2
shift

[ "$action" = "usage" ] && {
  echo "  Customised ls:"
  echo "    ls"
  echo "      shows items sorted by priority"
  echo "    ls ~/shared"
  echo "      shows items using a different TODO_DIR"
  echo ""
  exit
}

[ "$action" = "ls" ] && {
     python3 ${TODO_ACTIONS_DIR}/ls/ls.py "$TODO_DIR" $flag
}
