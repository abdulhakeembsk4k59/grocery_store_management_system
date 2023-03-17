# Grocery Store Management System | Day 5
# Implementation of User Interface:

## Follow these steps :
    1. Download this repository :
    2. copy `css`, `images`, `js` folders to your projects `ui` folder
    3. create `index.html` file and copy paste the below code :
    ```
    
<!DOCTYPE html>
<html>
    <head>
        <title> GSMS </title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
        <meta name="apple-mobile-web-app-capable" content="yes"/>
        <meta name="csrf-token" content="kmapods5wQ5L1hn7rcR9OPst7EsN0gC7SrHh3m9K"/>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/material-design-iconic-font/2.2.0/css/material-design-iconic-font.min.css">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:400,300,600,700">
        <link media="all" type="text/css" rel="stylesheet" href="css/bootstrap.min.css">
        <link media="all" type="text/css" rel="stylesheet" href="css/style.css?v=1.0">
        <link media="all" type="text/css" rel="stylesheet" href="css/sidebar-menu.css?v=1.0">
        <link media="all" type="text/css" rel="stylesheet" href="css/custom.css?v=1.3.3">
    </head>
    <body class="tooltips">
        <div class="container">

            <div class="header content rows-content-header">
                <button class="button-menu-mobile show-sidebar">
                    <i class="fa fa-bars"></i>
                </button>
                <div class="navbar navbar-default" role="navigation">
                    <div class="container">

                        <div class="navbar-collapse collapse">
                            <ul class="nav navbar-nav visible-lg visible-md limit-chars">
                                <ul class="breadcrumb">
                                    <a href="index.html">
                                        <i class="zmdi zmdi-view-dashboard zmdi-hc-fw" title="Orders"></i>
                                    </a>
                                    <a href="manage-product.html">
                                        <i class="zmdi zmdi-assignment zmdi-hc-fw" title="Products"></i>
                                    </a>
                                </ul>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <div class="right content-page">
                <div class="body content rows scroll-y">
                    <form class="form-horizontal" action="">
                        <div class="box-info full" id="taskFormContainer">
                            <h2>Grocery Store Management System</h2>
                            <div class="panel-body pt-0">
                                <div class="row mb-4">
                                    <div class="col-sm-12">
                                        <a href="order.html" class="btn btn-sm btn-primary pull-right ml-3">
                                            New Order
                                        </a>
                                        <a href="manage-product.html" class="btn btn-sm btn-primary pull-right">
                                            Manage Products
                                        </a>
                                    </div>
                                </div>
                                <table class="table table-bordered">
                                    <thead>
                                        <th>Date</th>
                                        <th>Order Number</th>
                                        <th>Customer Name</th>
                                        <th>Total Cost</th>
                                    </thead>
                                    <tbody>

                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </form>
                    <div class="modal " id="userProfileModal" role="dialog" >
                        <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-body text-center">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="modal fade-scale" id="myModal" role="dialog" data-backdrop="static">
                <div class="modal-dialog modal-lg">
                    <div class="modal-content">
                        <div class="modal-body text-center">
                            <img src="https://demo.test.cloint.com/assets/images/spinner.gif" width="40" style="margin: 60px auto;" alt="">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    
    <script src="js/packages/jquery.min.js"></script>
    <script src="js/custom/common.js"></script>
    <script src="js/custom/dashboard.js"></script>
</html>
```


### then you will get the output like this : 
<img src="https://i.ibb.co/GJPBgDP/image.png"/>

4. Create `order.html` page and paste this code :

```

<!DOCTYPE html>
<html>
<head>
    <title> GSMS </title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <meta name="apple-mobile-web-app-capable" content="yes"/>
    <meta name="csrf-token" content="kmapods5wQ5L1hn7rcR9OPst7EsN0gC7SrHh3m9K"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/material-design-iconic-font/2.2.0/css/material-design-iconic-font.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:400,300,600,700">
    <link media="all" type="text/css" rel="stylesheet" href="css/bootstrap.min.css">
    <link media="all" type="text/css" rel="stylesheet" href="css/style.css?v=1.0">
    <link media="all" type="text/css" rel="stylesheet" href="css/custom.css?v=1.3.3">
</head>
<body class="tooltips">
<div class="container">

    <div class="header content rows-content-header">
        <button class="button-menu-mobile show-sidebar">
            <i class="fa fa-bars"></i>
        </button>
        <div class="navbar navbar-default" role="navigation">
            <div class="container">

                <div class="navbar-collapse collapse">
                    <ul class="nav navbar-nav visible-lg visible-md limit-chars">
                        <ul class="breadcrumb">
                            <a href="index.html">
                                <i class="zmdi zmdi-view-dashboard zmdi-hc-fw" data-toggle="tooltip" data-placement="bottom" title="Dashboard"></i>
                            </a>
                            <a href="manage-product.html">
                                <i class="zmdi zmdi-assignment zmdi-hc-fw" data-toggle="tooltip" data-placement="bottom" title="Products"></i>
                            </a>
                        </ul>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <div class="right content-page">
        <div class="body content rows scroll-y">
            <form action="">
                <div class="box-info full" id="taskFormContainer">
                    <h2>New Order
                        <input name="customerName" id="customerName" type="text" class="form-control" placeholder="Customer Name" style="max-width:230px; float: right;margin-top: -11px">
                    </h2>
                    <div class="row" style="margin-bottom: 5px;margin-top: -10px;">
                        <div class="col-sm-12">
                            <div class="col-sm-4">
                                <label >Product</label>
                            </div>
                            <div class="col-sm-3">
                                <label >Price</label>
                            </div>
                            <div class="col-sm-2">
                                <label >Quantity</label>
                            </div>
                            <div class="col-sm-3">
                                <label >Total</label>
                                <button class="btn btn-sm btn-primary pull-right" style="margin-top: -5px" type="button" id="addMoreButton">Add More</button>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="product-box-extra" id="itemsInOrder">

                </div>

                <div>
                    <div class="row">
                        <div class="col-sm-12">
                            <div class="box-info full p-3 mb-3 mt-0">
                                <div class="col-sm-9 text-right">
                                    <span><b>Total</b></span>
                                </div>
                                <div class="col-sm-3">
                                    <b><input id="product_grand_total" name="product_grand_total" class="product-grand-total" value="0.0"></input> Rs</b>
                                    <button class="btn btn-sm btn-primary pull-right" type="button" id="saveOrder">Save</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </form>
            <div class="product-box hidden">
                <div class="row product-item">
                    <div class="col-sm-12">
                        <div class="box-info full p-3 mb-3 mt-0">
                            <div class="col-sm-4">
                                <select name="product" class="form-control cart-product" style="max-width: 250px"></select>
                            </div>
                            <div class="col-sm-3">
                                <input id="product_price" name="product_price" class="product-price" value="0.0"></input>
                            </div>
                            <div class="col-sm-2">
                                <input name="qty" type="number" min="1" placeholder="" class="form-control product-qty" value="1" style="max-width: 100px">
                            </div>
                            <div class="col-sm-3">
                                <input id="item_total" name="item_total" class="product-total"></input><span> Rs</span>
                                <button class="btn btn-sm btn-danger pull-right remove-row" type="button">Remove</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</body>
<script src="js/packages/jquery.min.js"></script>
<script src="js/custom/common.js"></script>
<script src="js/custom/order.js"></script>
</html>
```

### output would be like this : 
<img src="https://i.ibb.co/gV32Z9P/image.png"/>


5. now create a file named `magnage-product.html` :
```

<!DOCTYPE html>
<html>
<head>
    <title> GSMS </title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <meta name="apple-mobile-web-app-capable" content="yes"/>
    <meta name="csrf-token" content="kmapods5wQ5L1hn7rcR9OPst7EsN0gC7SrHh3m9K"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/material-design-iconic-font/2.2.0/css/material-design-iconic-font.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:400,300,600,700">
    <link media="all" type="text/css" rel="stylesheet" href="css/bootstrap.min.css">
    <link media="all" type="text/css" rel="stylesheet" href="css/style.css?v=1.0">
    <link media="all" type="text/css" rel="stylesheet" href="css/sidebar-menu.css?v=1.0">
    <link media="all" type="text/css" rel="stylesheet" href="css/custom.css?v=1.3.3">
</head>
<body class="tooltips">
<div class="container">

    <div class="header content rows-content-header">
        <button class="button-menu-mobile show-sidebar">
            <i class="fa fa-bars"></i>
        </button>
        <div class="navbar navbar-default" role="navigation">
            <div class="container">

                <div class="navbar-collapse collapse">
                    <ul class="nav navbar-nav visible-lg visible-md limit-chars">
                        <ul class="breadcrumb">
                            <a href="index.html">
                                <i class="zmdi zmdi-view-dashboard zmdi-hc-fw" title="Orders"></i>
                            </a>
                            <a href="manage-product.html">
                                <i class="zmdi zmdi-assignment zmdi-hc-fw" title="Products"></i>
                            </a>
                        </ul>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <div class="right content-page">
        <div class="body content rows scroll-y">
            <div class="box-info full" id="taskFormContainer">
                <h2>Manage Products</h2>
                <div class="panel-body pt-0">
                    <div class="row mb-4">
                        <div class="col-sm-12">
                            <button type="button" class="btn btn-sm btn-primary pull-right" data-toggle="modal" data-target="#productModal">
                                Add New Product
                            </button>
                        </div>
                    </div>
                    <table class="table table-bordered">
                        <thead>
                        <th>Name</th>
                        <th>Unit</th>
                        <th>Price Per Unit</th>
                        <th style="width: 150px">Action</th>
                        </thead>
                        <tbody>

                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>

    <div class="modal fade-scale" id="productModal" role="dialog" data-backdrop="static">
        <div class="modal-dialog ">
            <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title">Add New Product</h4>
                </div>
                <div class="modal-body">
                    <form id="productForm">
                        <input type="hidden" name="id" id="id" value="0">
                        <div class="row">
                            <div class="col-sm-12">
                                <div class="form-group">
                                    <label >Name</label>
                                    <input class="form-control" placeholder="Name" name="name" id="name" type="text" value="">
                                </div>
                            </div>
                            <div class="col-sm-12">
                                <div class="form-group">
                                    <label >Unit</label>
                                    <select name="uoms" id="uoms" class="form-control">
                                    </select>
                                </div>
                            </div>
                            <div class="col-sm-12">
                                <div class="form-group">
                                    <label >Price Per Unit</label>
                                    <input class="form-control" placeholder="Price Per Unit" name="price" id="price" type="text" value="">
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" id="saveProduct">Save</button>
                </div>
            </div>
        </div>
    </div>
</div>
<script src="js/packages/jquery.min.js"></script>
<script src="js/custom/common.js"></script>
<script src="js/custom/manage-product.js"></script>
<script src="js/packages/bootstrap.min.js"></script>
</body>
</html>
```

### output would be like : 
<img src="https://i.ibb.co/4gYxwsT/image.png"/>
