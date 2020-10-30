#!/bin/bash

TESTS=11;
PYTHON_SCRIPT="../task_A.py";

cd "task_A_tests" || return;

for (( i = 1; i <= TESTS; i++ )); do
    # cd "${i}_test" || continue;

    > "output_${i}.txt";
    python3 $PYTHON_SCRIPT < "input_${i}.txt" >> "output_${i}.txt";

    if cmp -s "output_${i}.txt" "answer_${i}.txt" ; then
        echo "$i test is OK";
    else
        echo "$i test is failed";
    fi

    #cd ..;
done

cd ..
