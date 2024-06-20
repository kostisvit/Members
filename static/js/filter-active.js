// Get the form and the select element
const form = document.getElementById('filter-form');
const select = form.querySelector('select[name="active"]');

// Add an event listener to the select element to submit the form on change
select.addEventListener('change', function() {
    form.submit();
});
