import qs from "qs";
import store from "../src/store";
import router from "../src/router";

const fastapi = (operation, url, params, success_callback, failure_callback) => {

  let method;
  let content_type;
  let body;

  let _url = import.meta.env.VITE_APP_SERVER_URL_ + url;

  if (operation === "login") {
    method = "post";
    content_type = "application/x-www-form-urlencoded";
    body = qs.stringify(params);
  } else {
    method = operation;
    content_type = "application/json";
    body = JSON.stringify(params);
  }

    let options = {
            method: method,
            headers: {
                "Content-Type": content_type
            }
        }

    const _access_token = store.state.access_token;
    if (_access_token){
      options.headers["Authorization"] = "Bearer " + _access_token;
    }


    if(method === 'get'){
        _url += "?" + new URLSearchParams(params);
    }
    else{
        options["body"] = body;
    }
    
    fetch(_url, options).then((response) => {
      if(response.status === 204){
        if (success_callback){
          success_callback();
        }
        return;
      }
        response
          .json()
          .then((json) => {
            if (response.status >= 200 && response.status < 300) {
              if (success_callback) {
                success_callback(json);
              }
            } 
            else if (operation != "login" && response.status === 401){
              store.commit("SetAccessToken", "");
              store.commit("SetUsername", "");
              store.commit("SetIsLogin", false);
              alert("An error occured with your login information. Please login again");
              router.push("/user-login");

            }
            else {
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