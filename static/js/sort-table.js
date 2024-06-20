document.addEventListener('DOMContentLoaded', () => {
    const table = document.getElementById('sortableTable');
    const headers = table.querySelectorAll('th');

    headers.forEach(header => {
        header.addEventListener('click', () => {
            const tableBody = table.querySelector('tbody');
            const rows = Array.from(tableBody.querySelectorAll('tr'));
            const index = Array.from(header.parentNode.children).indexOf(header);
            const type = header.getAttribute('data-type');
            const ascending = header.classList.contains('asc');
            
            // Remove sorting classes from all headers
            headers.forEach(th => th.classList.remove('asc', 'desc'));

            // Add sorting class to the current header
            header.classList.toggle('asc', !ascending);
            header.classList.toggle('desc', ascending);

            // Sorting function
            const compare = (a, b) => {
                const aText = a.children[index].textContent;
                const bText = b.children[index].textContent;

                if (type === 'number') {
                    return ascending ? bText - aText : aText - bText;
                } else {
                    return ascending
                        ? bText.localeCompare(aText)
                        : aText.localeCompare(bText);
                }
            };

            rows.sort(compare);

            // Append sorted rows to the table body
            rows.forEach(row => tableBody.appendChild(row));
        });
    });
});