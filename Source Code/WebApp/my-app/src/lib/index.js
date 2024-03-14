import { writable } from "svelte/store";

const stored = localStorage.getItem('token')
export const token = writable(stored)

token.subscribe(data => {
    if(data === null) {
        data = "";
    }
    localStorage.setItem('token', data);
})

export async function Login() {
    const storedToken = localStorage.getItem('token')
    var user;

    user = {
        "username": "testusername",
        "password": "testpassword"
    };

    const endpoint = "http://10.188.196.69:5000/login";
    const userdata = JSON.stringify(user)
  
    const response = await fetch(endpoint, {
        method: 'POST',
        mode: 'cors',
        body: userdata
    })

    if(!storedToken) {
        const json = await response.json();
        const newToken = json["token"]  
        token.set(newToken)
    }

    return response.ok;
}

export async function Register() {
    const user = {
        "username": "testusername",
        "password": "testpassword"
    };
  
    const endpoint = "http://10.188.196.69:5000/register";
    const userdata = JSON.stringify(user)
  
    const response = await fetch(endpoint, {
        method: 'POST',
        mode: 'cors',
        body: userdata
    })

    return response.ok;
}