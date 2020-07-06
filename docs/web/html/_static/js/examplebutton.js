function example(itemId, buttonId) {
    let item = document.getElementById(itemId);
    let button = document.getElementById(buttonId);
    if (item.style.display == "none") {
        item.style.display = "block";
        button.innerHTML = "Hide Example"
    } else {
        item.style.display = "none";
        button.innerHTML = "Show Example"
    }
}
