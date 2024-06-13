let file_div = document.getElementById('filecontent');

function load_data(lastmodtime) {
    $.ajax({
        url: 'http://127.0.0.1:8000/file-polling/',
        method: 'GET',
        data: {
            lastmod: lastmodtime
        },
        success: function (data) {
            console.log(data); 
            file_div.innerHTML += `<h4>${data.data}</h4>`;
            file_div.innerHTML += `<hr/>`;
            lastmodtime = data.filetime;
            load_data(lastmodtime);
        },
        error: function (xhr, status, error) {
            console.log('Error loading data:', status, error);
            file_div.innerHTML = '<h2 class="text-danger">Error getting data</h2>';
            setTimeout(() => load_data(0), 5000); 
        }
    });
}

load_data(0); 
