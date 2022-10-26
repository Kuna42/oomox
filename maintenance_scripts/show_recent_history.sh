#!/usr/bin/env bash
set -euo pipefail

style="default"
if [[ "${1:-}" = '-c' ]] ; then
	style="compact"
	shift
fi

result=$(git log \
	--pretty=tformat:"%Cred%D%Creset %ad %Cgreen%h %Cblue%an %Creset%s" \
	--date='format:%Y-%m-%d' \
	--color=always \
	"$(git tag | grep -v gtk | sort -V | tail -n1)"~1.. \
	"$@" \
)

if [[ "${style}" = "none" ]] ; then
	echo "$result"
else
	echo "Notable changes:"
	echo "$result" \
	| grep -v -i -E \
		-e "(typing|typehint|coverage|github|docker|vulture)" \
		-e "actionless\s[^[:print:]]\[m(doc|chore|test|style|Revert|Merge|refactor)" \
	| sed \
		-E "s/[^[:print:]]\[31m[[:print:]]+[^[:print:]]\[m//g"
	echo
	echo "Submodule changes:"
	grep submodule <<< "$result"
	echo
	echo "Previous release:"
	echo "$result" | tail -n1
fi
