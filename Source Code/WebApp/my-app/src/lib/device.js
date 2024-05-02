
export async function GetDevices() {
    const user = {
        "token": "thiswillberandomsoon"
    };
  
    const endpoint = "http://127.0.0.1/user";
    const userdata = JSON.stringify(user)
  
    const response = await fetch(endpoint, {
        method: 'POST',
        mode: 'cors',
        body: userdata
    })
  
    const json = await response.json()
    const devices = json["devices"]

    return devices;
}