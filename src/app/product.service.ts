import { Injectable } from '@angular/core';
import { Product } from './product';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  products: Product[] = [{id:1,product_name:"Laptop",base_price:30000,product_category:"Electronic",product_details:"Lenovo core i3 5th Generation",product_photo_link:"assets/laptop.png",approval:true},
                        {id:2,product_name:"Bike",base_price:230000,product_category:"Electronic",product_details:"R15",product_photo_link:"assets/bike.png",approval:true},
                        {id:3,product_name:"T-Shirt",base_price:300,product_category:"Cloths",product_details:"Classical T-shirt",product_photo_link:"assets/t-shirt.jpg",approval:true},
                        {id:4,product_name:"SmartPhone",base_price:10000,product_category:"Electronic",product_details:"Walton primo W3",product_photo_link:"assets/smartphones.jpg",approval:true},
                        {id:5,product_name:"T-shirt2",base_price:250,product_category:"Cloths",product_details:"Beautiful t-shirt",product_photo_link:"assets/t-shirt2.jpg",approval:false},
                        {id:6,product_name:"T-shirt3",base_price:200,product_category:"Cloths",product_details:"Cotton sleeves t-shirt",product_photo_link:"assets/t-shirt3.jpg",approval:true},
                      ]

productToBeShown  = new Product();
  constructor() { }

getProducts():Product[]{
  return this.products;
}
setProductToBeShown(product:Product){
  this.productToBeShown=product;
}
getProductToBeShown():Product{
  return this.productToBeShown;
}
showProduct(){
  console.log("product: "+this.productToBeShown);
}

}
