#!/usr/bin/env bash

REPO_URL=`git config --local --get svn-remote.svn.url | awk -F '@' '{print "http://"$2}'`

help()
{
	cat << FLAG
git2svn [cmd] [option]

e.g.
git2svn br [url [\$branch_name]]
git2svn tag [url [\$tag_name]]
FLAG
}

br()
{
  if [ "$2" = "url" ]; then
    echo "$REPO_URL/branches/$3"
  else
      git branch -a | grep "remotes/origin"  | grep -v "/tags/"
  fi
}

tag()
{
  if [ "$2" = "url" ]; then
    echo "$REPO_URL/tags/$3"
  else
    git branch -a | grep "remotes/origin/tags" 
  fi
}


case $1 in
  'br') br $@;;
  'tag') tag $@;;
  *) help;;
esac
