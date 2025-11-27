from pyscript import display  # type: ignore
from js import document  # type: ignore

club_data = {
    'CommArts Club': {
        'Description': 'Develop communication, media, and artistic expression skills.',
        'Meeting Time': 'Every Tuesday 2:00-3:00 PM',
        'Location': '4th Floor Classrooms (any classroom)',
        'Club Moderator': 'Mrs. Morales',
        'Number of Members': 21,
        'Category': 'Arts and Culture/Academic'
    },
    'Social Sciences Club': {
        'Description': 'Exploring history, politics, and human society.',
        'Meeting Time': 'Every Monday 2:30-3:30 PM',
        'Location': '6th Floor Classrooms (any classroom)',
        'Club Moderator': 'Mr. Marutani',
        'Number of Members': 28,
        'Category': 'Academic'
    },
    'Science Club': {
        'Description': 'Hands-on experiments and exploration of scientific concepts.',
        'Meeting Time': 'Every Wednesday 1:30-2:30 PM',
        'Location': 'Chemistry Lab',
        'Club Moderator': 'Ms. Zabala',
        'Number of Members': 27,
        'Category': 'Academic'
    },
    'Math Club': {
        'Description': 'Enhancing mathematical skills through competitions and activities.',
        'Meeting Time': 'Every Friday 2:30-3:30 PM',
        'Location': '5th Floor Classrooms (any classroom)',
        'Club Moderator': 'Mr. Ferma',
        'Number of Members': 28,
        'Category': 'Academic'
    }
}

def display_club_info(event):
    selected = document.getElementById("club-select").value
    info = club_data.get(selected, None)

    output = document.getElementById("output")

    if info:
        html = f"<h4>{selected}</h4><ul>"
        for key, value in info.items():
            html += f"<li><strong>{key}:</strong> {value}</li>"
        html += "</ul>"
    else:
        html = "<p>Please select a valid club.</p>"

    output.innerHTML = html

    # Sir if you're reading this, I didn't know which teachers are the club moderators, so I just put in the teachers I know. I also didn't know what rooms they use so I put random rooms instead.
