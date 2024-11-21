
let currentPage = 1;
const totalPages = 5;

const prevButton = document.querySelector('.prev-btn');
const nextButton = document.querySelector('.next-btn');

function updatePagination() {
    prevButton.disabled = currentPage === 1;
    nextButton.disabled = currentPage === totalPages;
    console.log(`현재 페이지: ${currentPage}`);
        }

prevButton.addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage--;
        updatePagination();
            }
        });

nextButton.addEventListener('click', () => {
    if (currentPage < totalPages) {
        currentPage++;
        updatePagination();
            }
        });

updatePagination();
