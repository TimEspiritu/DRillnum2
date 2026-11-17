from pyscript import document

BatFamily = {"Alfred Pennyworth", "Richard Grayson", "Jason Todd"}
JusticeLeague = {"Bruce Wayne", "Clark Kent", "Princess Diana"}
XMen = {"Charles Xavier", "Scott Summers", "Jean Grey"}
Avengers = {"Tony Stark", "Steve Rogers", "Bruce Banner"}

master_set = BatFamily | JusticeLeague | XMen | Avengers

def add_member(event):
    global master_set  
    
    first = document.querySelector("#first_name").value.strip()
    last = document.querySelector("#last_name").value.strip()

    if first and last:
        master_set.add(f"{first} {last}")

    members_list = "<br>".join(sorted(master_set))
    document.querySelector("#output").innerHTML = (
        f"All members:<br>{members_list}<br><br>Total members: {len(master_set)}"
    )