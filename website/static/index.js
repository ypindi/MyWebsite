function deleteNote(noteId){
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({noteId: noteId}),
    }).then((_res) => {
        window.location.href = "/";
        // reload the window after deleting the note
    });
}

// it is making a post request to the delete-note end point.
// after that window is reloading the page to remove the old deleted note.
// it is redirecting us to the home page which is internally reloading the page.