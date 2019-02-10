// cart:
var shopUrl = "/shop/";
var filter = {
    category: null,
    ordering: null,
}
function onGetCartItems(){
    if(localStorage.getItem("cartItems")){
        return JSON.parse(localStorage.getItem("cartItems"))
    }
    return [];
}
function onUpdateCartItems(items){
    localStorage.setItem("cartItems", JSON.stringify(items));
}
function onAddToCart(item){
    let items = [];
    item.count = 1;//default count is 1;
    if(localStorage.getItem("cartItems")){
        items = JSON.parse(localStorage.getItem("cartItems"));
        // console.log(items.find(i=>i.id == item.id))
        if(items.find(i=>i.id == item.id) == undefined){
            items.push(item);
            toastr.success('Товар добавлен в корзину')
        }else{
            toastr.warning('Товар уже есть в корзине')
        }
    }else{
        items.push(item);
        toastr.success('Товар добавлен в корзину')
    }
    onUpdateCartItems(items)
}
function onRemoveFromCart(item_id){
    // console.log(item_id)
    var items = onGetCartItems();
    var index = items.findIndex(item=>item.id == item_id);
    if(index > -1){
        items.splice(index, 1);
        onUpdateCartItems(items)
    }
    // console.log(items);
}
function onUpdateCartItem(item_id, newcount){
    items = onGetCartItems();
    // console.log("Update", items, item_id, newcount)
    var searchitem = items.find(item=>{ return item.id == item_id; });
    // console.log("search", searchitem)
    if(searchitem != undefined){
        searchitem.count = newcount;
        onUpdateCartItems(items)
    }
}
// Read a page's GET URL variables and return them as an associative array.
function getUrlVars(){
    var vars = [], hash;
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for(var i = 0; i < hashes.length; i++){
        hash = hashes[i].split('=');
        vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }
    return vars;
}
function setUrlVar(query){
    var vars = [], hash;
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    if(!window.location.href.includes('?'))
        hashes = [];
    var exist = false;
    for(var i = 0; i < hashes.length; i++){
        hash = hashes[i].split('=');
        if(query.name == hash[0]){
            hash[1] = query.value;//change value of query
            exist = true;
        }
        vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }
    if(!exist){
        hash = [query.name, query.value];
        vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }
    let str = shopUrl;
    for(var i = 0; i < vars.length; i++){
        let before = i==0?'?':'&';
        str+=before+vars[i]+'='+vars[vars[i]];
    }
    // console.log('str:', vars);
    return str;
}