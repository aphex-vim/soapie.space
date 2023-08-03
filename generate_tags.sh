#!/bin/bash
# generated md files for each tag present on the site
POSTS_DIR="_blog"

# array to store the extracted tags
tags=()

# loop through each post in the directory
for post in "$POSTS_DIR"/*.md; do
  # extract the tags from the front matter
  post_tags=$(awk '/^tags: / {for(i=2;i<=NF;i++){print $i}}' "$post")

  # loop through each tag and add it to the main tags array
  while IFS= read -r tag; do
    tags+=("$tag")
  done <<< "$post_tags"
done

# remove duplicate tags
unique_tags=($(printf '%s\n' "${tags[@]}" | sort -u))

# making md files for each tag
for tag in "${unique_tags[@]}"; do
    printf -- "---\nlayout: tag\ntag-name: $tag\n---" > _tags/$tag.md
done