//On load
(function() {
    // modal.classList.add('is-active')
 })();


 function addSong(id){
    console.log("Show modal for playlist with id of: " + id)
    const modal = document.getElementById('add-modal')
    modal.classList.add('is-active')

    const songInput = document.getElementById('song-input')
    songInput.focus()

    const playlistIdInput = document.getElementById('playlist-id-input')
    playlistIdInput.value = id
 }

 function closeModal(){
    const modal = document.getElementById('add-modal')
    modal.classList.remove('is-active')
 }