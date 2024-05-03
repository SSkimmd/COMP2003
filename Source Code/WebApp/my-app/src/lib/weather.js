
export async function GetLocation() {
    const user = {
        "token": "thiswillberandomsoon"
    };
    const endpoint = "http://127.0.0.1:5000/user";
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
    const endpoint = "http://127.0.0.1:5000/user";
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
    const endpoint = "http://127.0.0.1:5000/weather";
    const userdata = JSON.stringify(user)
  
    const response = await fetch(endpoint, {
        method: 'POST',
        mode: 'cors',
        body: userdata
    })

    const json = await response.json()
    return json['kind']; //kind
}
export async function GetMoon() {
    const user = {
        "token": "thiswillberandomsoon"
    };
  
    const endpoint = "http://127.0.0.1:5000/weather";
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
  
    const endpoint = "http://127.0.0.1:5000/weather";
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
  
    const endpoint = "http://127.0.0.1:5000/weather";
    const userdata = JSON.stringify(user)
  
    const response = await fetch(endpoint, {
        method: 'POST',
        mode: 'cors',
        body: userdata
    })

    const json = await response.json()
    

    return json['temperature'];
}

export async function GetSunRise() {
    const user = {
        "token": "thiswillberandomsoon"
    };
  
    const endpoint = "http://127.0.0.1:5000/weather";
    const userdata = JSON.stringify(user)
  
    const response = await fetch(endpoint, {
        method: 'POST',
        mode: 'cors',
        body: userdata
    })

    const json = await response.json()
    

    return json['sunrise'];
}


export async function GetSunSet() {
    const user = {
        "token": "thiswillberandomsoon"
    };
  
    const endpoint = "http://127.0.0.1:5000/weather";
    const userdata = JSON.stringify(user)
  
    const response = await fetch(endpoint, {
        method: 'POST',
        mode: 'cors',
        body: userdata
    })

    const json = await response.json()
    

    return json['sunset'];
}

export async function GetUV() {
    const user = {
        "token": "thiswillberandomsoon"
    };
  
    const endpoint = "http://127.0.0.1:5000/weather";
    const userdata = JSON.stringify(user)
  
    const response = await fetch(endpoint, {
        method: 'POST',
        mode: 'cors',
        body: userdata
    })

    const json = await response.json()
    

    return json['ultraviolet'];
}


export async function GetWind() {
    const user = {
        "token": "thiswillberandomsoon"
    };
  
    const endpoint = "http://127.0.0.1:5000/weather";
    const userdata = JSON.stringify(user)
  
    const response = await fetch(endpoint, {
        method: 'POST',
        mode: 'cors',
        body: userdata
    })

    const json = await response.json()
    

    return json['wind_speed'];

}

export async function GetKind1() {
    const user = {
        "token": "thiswillberandomsoon"
    };
  
    const endpoint = "http://127.0.0.1:5000/weather";
    const userdata = JSON.stringify(user)
  
    const response = await fetch(endpoint, {
        method: 'POST',
        mode: 'cors',
        body: userdata
    })

    const json = await response.json()
    

    return json['kind1'];
}

export async function GetKind2() {
    const user = {
        "token": "thiswillberandomsoon"
    };
  
    const endpoint = "http://127.0.0.1:5000/weather";
    const userdata = JSON.stringify(user)
  
    const response = await fetch(endpoint, {
        method: 'POST',
        mode: 'cors',
        body: userdata
    })

    const json = await response.json()
    

    return json['kind2'];
}

export async function GetKind3() {
    const user = {
        "token": "thiswillberandomsoon"
    };
  
    const endpoint = "http://127.0.0.1:5000/weather";
    const userdata = JSON.stringify(user)
  
    const response = await fetch(endpoint, {
        method: 'POST',
        mode: 'cors',
        body: userdata
    })

    const json = await response.json()
    

    return json['kind3'];
}

export async function GetKind4() {
    const user = {
        "token": "thiswillberandomsoon"
    };
  
    const endpoint = "http://127.0.0.1:5000/weather";
    const userdata = JSON.stringify(user)
  
    const response = await fetch(endpoint, {
        method: 'POST',
        mode: 'cors',
        body: userdata
    })

    const json = await response.json()
    

    return json['kind4'];
}