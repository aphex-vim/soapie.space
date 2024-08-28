#!/bin/bash
# error checking
if [ $# -ne 1 ]; then
    echo "$0: must provide a slugified title"
    echo "usage: $0 <my-blog-post-title>"
else
    title=$1
fi

create_new_draft_from_template() {
    echo "---"
    echo "layout: post"
    echo "title: $title"
    echo "date: $(date +%Y-%0m-%0d)"
    echo "tags:"
    echo "---"
}


# create new draft
new_draft_path="_drafts/$(date +%Y-%0m-%0d-$title.md)"

# echo template into new draft
create_new_draft_from_template > $new_draft_path