import VueCookies from 'vue-cookies';

const APIBase = "/api";

const jsonRequest = async function(url, params, method) {
    const myHeaders = new Headers();
    myHeaders.append("X-CSRFToken", VueCookies.get("csrftoken"));
    myHeaders.append('Content-Type', 'application/json');

    const requestOptions = {
        method: method || 'POST',
        headers: myHeaders
    };

    if (params) requestOptions.body = JSON.stringify(params);

    let response = await fetch(APIBase + url, requestOptions);

    return await response.text().then(function(text) {
        return text ? JSON.parse(text) : {}
    })
};

export const deleteJsonRequest = async function(url) {
    return await jsonRequest(url, null, 'DELETE');
};

export const  putJsonRequest = async function(url, params) {
    return await jsonRequest(url, params, 'PUT');
};

export const  postJsonRequest = async function(url, params) {
    return await jsonRequest(url, params, 'POST');
};

export const  getJsonRequest = async function(url) {
    return await jsonRequest(url, null, 'GET');
};

export const  patchJsonRequest = async function(url, params) {
    return await jsonRequest(url, params, 'PATCH');
};

