// cart:
console.log("base.js")
function addToCart(item){
    let items = [];
    if(localStorage.getItem("cartItems")){
        items = JSON.parse(localStorage.getItem("cartItems"));
        console.log(items.find(i=>i.id == item.id))
        if(items.find(i=>i.id == item.id) == undefined){
            items.push(item)
        }else{
            alert("you")
        }
    }else{
        items.push(item);
    }
    console.log(items)
    localStorage.setItem("cartItems", JSON.stringify(items));
}
function getCartItems(){
    if(localStorage.getItem("cartItems")){
        return JSON.parse(localStorage.getItem("cartItems"))
    }
    return [];
}