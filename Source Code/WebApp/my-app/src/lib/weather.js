
export async function GetLocation() {
    const user = {
        "token": "thiswillberandomsoon"
    };
  
    const endpoint = "http://10.188.196.69:5000/user";
    const userdata = JSON.stringify(user)
  
    const response = await fetch(endpoint, {
        method: 'POST',
        mode: 'cors',
        body: userdata
    })
  
    const json = await response.json()
    const location = json["location"]  

    return location;
}

/**
 * @param {string} newLocation
 */
export async function UpdateLocation(newLocation) {
    const user = {
        "token": "thiswillberandomsoon",
        "location": newLocation
    };
  
    const endpoint = "http://10.188.196.69:5000/user";
    const userdata = JSON.stringify(user)
  
    const response = await fetch(endpoint, {
        method: 'PATCH',
        mode: 'cors',
        body: userdata
    })

    return response.ok;
}

export async function GetWeather() {
    const user = {
        "token": "thiswillberandomsoon"
    };
  
    const endpoint = "http://10.188.196.69:5000/weather";
    const userdata = JSON.stringify(user)
  
    const response = await fetch(endpoint, {
        method: 'POST',
        mode: 'cors',
        body: userdata
    })

    const json = await response.json()
    

    return json['kind'];
}
export async function GetMoon() {
    const user = {
        "token": "thiswillberandomsoon"
    };
  
    const endpoint = "http://10.188.196.69:5000/weather";
    const userdata = JSON.stringify(user)
  
    const response = await fetch(endpoint, {
        method: 'POST',
        mode: 'cors',
        body: userdata
    })

    const json = await response.json()
    

    return json['moon_phase'];
}
export async function GetHumidity() {
    const user = {
        "token": "thiswillberandomsoon"
    };
  
    const endpoint = "http://10.188.196.69:5000/weather";
    const userdata = JSON.stringify(user)
  
    const response = await fetch(endpoint, {
        method: 'POST',
        mode: 'cors',
        body: userdata
    })

    const json = await response.json()
    

    return json['humidity'];
}

export async function GetTemp() {
    const user = {
        "token": "thiswillberandomsoon"
    };
  
    const endpoint = "http://10.188.196.69:5000/weather";
    const userdata = JSON.stringify(user)
  
    const response = await fetch(endpoint, {
        method: 'POST',
        mode: 'cors',
        body: userdata
    })

    const json = await response.json()
    

    return json['temperature'];
}