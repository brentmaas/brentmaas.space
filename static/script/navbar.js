const navbarSessionStorageKey = "navbar-open";

function setNavbar(){
    document.getElementById("navbar-expanded").hidden = !isNavbarOpen;
    document.getElementById("navbar-contracted").hidden = isNavbarOpen;
    var contentElement = document.getElementById("content");
    if(isNavbarOpen){
        contentElement.classList.add("content-contracted");
    }else{
        contentElement.classList.remove("content-contracted");
    }
}

function toggleNavbar(){
    isNavbarOpen = !isNavbarOpen;
    sessionStorage.setItem(navbarSessionStorageKey, isNavbarOpen);
    setNavbar();
}

function getNavbarStatusFromSessionStorage(){
    var navbarStatus = sessionStorage.getItem(navbarSessionStorageKey);
    if(navbarStatus === null){
        return true;
    }else{
        return navbarStatus === "true";
    }
}

var isNavbarOpen = getNavbarStatusFromSessionStorage();