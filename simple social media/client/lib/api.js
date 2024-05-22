const fastapi = (operation, url, params, success_callback, failure_callback) => {
    let method = operation;
    let _url = "http://localhost:8000" + url;

    let options = {
            method: method,
            headers: {
                "Content-Type": "application/json"
            }
        }

    
    if(method === 'get'){
        _url += "?" + new URLSearchParams(params);
    }
    else{
        options["body"] = JSON.stringify(params);
    }
    
    fetch(_url, options).then((response) => {
        response
          .json()
          .then((json) => {
            if (response.status >= 200 && response.status < 300) {
              if (success_callback) {
                success_callback(json);
              }
            } else {
              if (failure_callback) {
                failure_callback(json);
              } else {
                alert(JSON.stringify(json));
              }
            }
          })
          .catch((error) => {
            alert(JSON.stringify(error));
          });
      });
    };
    

export default fastapi;