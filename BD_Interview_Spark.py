# with dedup as (
#   select
#   product.ProductKey,
#   row_number() over (Partition by productKey Order by productKey desc) as rn
#   from `project-daf89c66-e0a7-43f3-b01.BD_Interview.Product` product
# )
# select * from dedup where rn>1;

# SELECT sales.*, calender.*,channel.*,geography.*, product.*,productCategory.*,productSubCategory.*,promotion.*,stores.*
# FROM `project-daf89c66-e0a7-43f3-b01.BD_Interview.Sales` sales JOIN
# `project-daf89c66-e0a7-43f3-b01.BD_Interview.Calender` calender on sales.DateKey = calender.DateKey JOIN
# `project-daf89c66-e0a7-43f3-b01.BD_Interview.Channel` channel on sales.channelKey=channel.Channel JOIN
# `project-daf89c66-e0a7-43f3-b01.BD_Interview.Stores` stores on sales.StoreKey = stores.StoreKey JOIN
# `project-daf89c66-e0a7-43f3-b01.BD_Interview.Geography` geography on stores.GeographyKey = geography.GeographyKey JOIN
# `project-daf89c66-e0a7-43f3-b01.BD_Interview.Product` product on sales.ProductKey = product.ProductKey JOIN
# `project-daf89c66-e0a7-43f3-b01.BD_Interview.ProductSubcategory` productSubCategory on product.ProductSubcategoryKey = productSubCategory.ProductSubcategoryKey JOIN
# `project-daf89c66-e0a7-43f3-b01.BD_Interview.ProductCategory` productCategory on productSubCategory.ProductCategoryKey = productCategory.ProductCategoryKey JOIN
# `project-daf89c66-e0a7-43f3-b01.BD_Interview.Promotion` promotion on sales.PromotionKey=promotion.PromotionKey;

# -- total sales, total quantity, avg(sellin price),asp

# SELECT calender.Year, calender.MonthOfYear,calender.MonthName, SUM(sales.salesAmount) as total_salesAmount, SUM(sales.salesQuantity) as total_SalesQuantity, productSubCategory.ProductSubCategory as subCategory, ROUND(SUM(sales.salesAmount)/SUM(sales.salesQuantity),2) 
# from `project-daf89c66-e0a7-43f3-b01.BD_Interview.Sales` sales 
# JOIN 
# `project-daf89c66-e0a7-43f3-b01.BD_Interview.Calender` calender
# ON sales.DateKey = calender.DateKey join
# `project-daf89c66-e0a7-43f3-b01.BD_Interview.Product` product on sales.ProductKey = product.ProductKey JOIN
# `project-daf89c66-e0a7-43f3-b01.BD_Interview.ProductSubcategory` productSubCategory on product.ProductSubcategoryKey = productSubCategory.ProductSubcategoryKey JOIN
# `project-daf89c66-e0a7-43f3-b01.BD_Interview.ProductCategory` productCategory on productSubCategory.ProductCategoryKey = productCategory.ProductCategoryKey
# GROUP BY calender.Year, calender.MonthOfYear,calender.MonthName,subCategory
# ORDER BY calender.Year,calender.MonthOfYear,calender.MonthName,subCategory DESC;
