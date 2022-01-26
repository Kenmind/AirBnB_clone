#!/usr/bin/env bash
# Generates an AUTHORS file that lists all individuals who
#+ have contributed to this repository

set -e

cd "$(dirname "$(readlink -f "$BASH_SOURCE")")/.."

{
	cat <<- 'EOH'
				# This file lists all individuals having contributed content to this repository.
				# For how it is generated see 'Auth-Gen/auth_gen.sh'.
	EOH
	echo
	git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} > AUTHORS
