"""
auth spencer-maaaaan
desc calculates fields to be used in make_tables.py from rows, returns a 2d array of the fields for the index table
"""
import subprocess
import json

# calculating all the needed fields to generate the index table
def make_index_arrays(rows):
    
    #generating the list of titles/links to be used later
    links=get_links()

    # defining some vars to calculate the netchange per episode
    last_ep_end_rank=0
    last_ep_num=int(rows[-1][1])
    episode_numbers=range(1,last_ep_num+1)
    changes_in_rank=[]
    
    # finding the net change in rank between episodes
    for i in episode_numbers:
        cur_ep=[game for game in rows if int(game[1])==i]
        last_game_end_rank=int(cur_ep[-1][2])

        changes_in_rank.append(last_game_end_rank-last_ep_end_rank)
        last_ep_end_rank=last_game_end_rank

    # formatting each row of the index table as an array
    outrows=[]
    for i in episode_numbers:
        # changing the type of the change in rank to str and adding a + if positive
        change=changes_in_rank[i-1]

        if change > 0:
            changes_in_rank[i-1]="+"+str(change)
        else:
            changes_in_rank[i-1]=str(change)

        outrows.append(["Episode "+str(i),changes_in_rank[i-1],links[i-1]])

    # adding all the rows to the 2d ouput array
    index_table=[["Episode #","Net Change","Episode Title/Link"]]
    for row in outrows:
        index_table.append(row)

    return index_table


# returns a list of titles that are html links to their respective videos
def get_links():
    
    # running youtube-dl with some options to get a json of the videos in the playlist
    with open("/tmp/episode_info.json", "w") as f:
        subprocess.run(["youtube-dl", "-j", "--flat-playlist", "https://www.youtube.com/playlist?list=PL3Hg1a3VjI1aOI1tB6gjSDO1tNUtdTaXQ"], stdout=f)

    # for each video, extracting information from json and adding to title/link list
    links=[]
    with open("/tmp/episode_info.json", "r") as f:
        for line in f.readlines():
            episode=json.loads(line)
            links.append("<a href=\"https://www.youtube.com/watch?v="+episode["url"]+"\">"+episode["title"]+"</a>")

    return links