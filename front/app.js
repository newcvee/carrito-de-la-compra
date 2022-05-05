console.log("entrando en app.js");
let app = Vue.createApp({
  data() {
    return {
      userName: "Camelia",
      items: [
        { product: "", unit: "1", price: "1.2", completed: false },
        { product: "queso", unit: "2", price: "1.85", completed: false },
        { product: "leche", unit: "12", price: "0.84", completed: false },
      ],
      showAllItems: true,
      showDiscount: false,
      newProductName: "",
      newUnid: "",
      newPrice: ""
    };
  },
  computed: {
    totalWithDiscount() {
      let total = this.totalInvoice;
      let disc = this.cashDiscount;

      totalWithDisc = total - disc;
      return totalWithDisc.toFixed(2);
    },
    totalInvoice() {
      total = 0;

      for (element of this.filteredItems) {
        total += element.unit * element["price"];
      }
      return total.toFixed(2);
    },
    countProducts() {
      lengthItems = 0;
      for (this.item of this.items) {
        if (this.item.completed == false) {
          lengthItems += 1;
        }
      }
      return lengthItems;
    },
    accountInCurrency() {
      return "€";
    },
    filteredItems() {
      let filtered = [];
      for (item of this.items) {
        if (!item.completed) {
          filtered.push(item);
        }
      }
      return filtered;
    },
    cashDiscount() {
      let discount = 3;
      return discount.toFixed(2);
    },
  },
  mounted() {
    this.loadData();
  },
  methods: {
    totalProduct(item) {
      sumatory_total = item.unit * item.price;
      return sumatory_total.toFixed(2);
    },
    completeButton(item) {
      item.completed = true;
    },
    pendingButton(item) {
      item.completed = false;
    },
    async loadData() {
      endpoint = "http://192.168.21.62:5000/shopping-cart";

      let response = await fetch(endpoint);
      let loadData = await response.json();

      this.items = loadData;
    },
    
    async addNewProduct(){
      let newProduct = {product: this.newProductName, unit: this.newUnid, price: this.newPrice, completed: false}
      

      const settings = {
        method: "POST",
        body: JSON.stringify(newProduct),
      };
      let response = await fetch (
        "http://192.168.21.62:5000/shopping-cart",
        settings
      );
      
      this.newProductName= "",
      this.newUnid= "",
      this.newPrice=""
      
      this.items.push(newProduct);


    }
  },
});
app.mount("#vue-app");
