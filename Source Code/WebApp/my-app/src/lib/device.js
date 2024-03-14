
export async function GetDevices() {
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
    const devices = json["devices"]

    return devices;
}