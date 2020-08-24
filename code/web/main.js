function display_weather() {
    let place = document.getElementById('location');
    eel.get_weather(place)(callback);
}

function callback(result) {
    document.getElementById('show').value = result;
}