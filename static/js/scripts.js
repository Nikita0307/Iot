function send_data() {
    $.ajax({
        type: 'GET',
        url: '/connect',
        dataType: 'json',
        connectType: 'application/json',
        data: {
            "value": document.getElementById("value").value,
            "name": document.getElementById("name").value,
        },
        success: function (response) {
            console.log(response)
        }
    });
}

function send_data_2() {
    $.ajax({
        type: 'GET',
        url: '/connect_2',
        dataType: 'json',
        connectType: 'application/json',
        data: {
            "value": document.getElementById("value").value,
        },
        success: function (response) {
            console.log(response)
        }
    });
}

function day() {
    $.ajax({
        type: 'GET',
        url: '/day_light_up',
        dataType: 'json',
        connectType: 'application/json',
        data: {
            "value": document.getElementById("value").value,
            "name": document.getElementById("name").value,
        },
        success: function (response) {
            console.log(response)
        }
    });
}

function night() {
    $.ajax({
        type: 'GET',
        url: '/night_light_up',
        dataType: 'json',
        connectType: 'application/json',
        data: {
            "value": document.getElementById("value").value,
            "name": document.getElementById("name").value,
        },
        success: function (response) {
            console.log(response)
        }
    });
}

function get_temperature() {
    $.ajax({
        type: 'GET',
        url: '/get_temp',
        dataType: 'json',
        connectType: 'application/json',
        data: {
            "value1": document.getElementById("value1").value,
        },
        success: function (response) {
            console.log(response)
        }
    });
}

function get_lightning() {
    $.ajax({
        type: 'GET',
        url: '/get_light',
        dataType: 'json',
        connectType: 'application/json',
        data: {
            "value4": document.getElementById("value4").value,
            "check2": Number(document.getElementById("check2").checked)
        },
        success: function (response) {
            console.log(response)
        }
    });
}

function get_humidity() {
    $.ajax({
        type: 'GET',
        url: '/get_humidity',
        dataType: 'json',
        connectType: 'application/json',
        data: {
            "value2": document.getElementById("value2").value,
        },
        success: function (response) {
            console.log(response)
        }
    });
}

function get_air_condition() {
    $.ajax({
        type: 'GET',
        url: '/get_air_condition',
        dataType: 'json',
        connectType: 'application/json',
        data: {
            "value3": document.getElementById("value3").value,
            "check1": Number(document.getElementById("check1").checked)
        },
        success: function (response) {
            console.log(response)
        }
    });
}


//Warehouse

function get_water() {
    $.ajax({
        type: 'GET',
        url: '/get_water',
        dataType: 'json',
        connectType: 'application/json',
        data: {
            "valueWater": document.getElementById("value1").value,
        },
        success: function (response) {
            console.log(response)
        }
    });
}

function get_seeds() {
    $.ajax({
        type: 'GET',
        url: '/get_seed',
        dataType: 'json',
        connectType: 'application/json',
        data: {
            "valueSeeds": document.getElementById("value2").value,
        },
        success: function (response) {
            console.log(response)
        }
    });
}

function get_fertilizer() {
    $.ajax({
        type: 'GET',
        url: '/get_fertilizer',
        dataType: 'json',
        connectType: 'application/json',
        data: {
            "valueFert": document.getElementById("value3").value,
        },
        success: function (response) {
            console.log(response)
        }
    });
}

function get_components() {
    $.ajax({
        type: 'GET',
        url: '/get_components',
        dataType: 'json',
        connectType: 'application/json',
        data: {
            "valueComp": document.getElementById("value4").value,
        },
        success: function (response) {
            console.log(response)
        }
    });
}