document.getElementById("search-button").addEventListener("click", () => {
    const input = document.getElementById("search-input").value.toLowerCase(); 
    const boxes = document.querySelectorAll(".site-img"); 

    boxes.forEach(box => {
        const tag = box.dataset.tag.toLowerCase(); 
        if (tag.includes(input)) {
            box.style.display = "block";
        } else {
            box.style.display = "none"; 
        }
    });

    if (!input) {
        boxes.forEach(box => box.style.display = "block");
    }
});
