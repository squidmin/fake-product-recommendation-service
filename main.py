from fastapi import FastAPI, Path
from random import randint

from pydantic import BaseModel

from data_objects import Product

app = FastAPI()


# Generate random product names
def generate_recommendation_name():
    adjectives = ["Awesome", "Fantastic", "Stylish", "Trendy", "Cozy"]
    nouns = ["Shirt", "Hat", "Watch", "Shoes", "Bag"]
    return f"{adjectives[randint(0, len(adjectives)-1)]} {nouns[randint(0, len(nouns)-1)]}"


# Endpoint for purchase history recommendations
@app.get("/products/{product_id}/purchaseHistory")
async def get_purchase_history_recommendations(product_id: int = Path(..., description="ID of the product")):
    # Simulate purchase history recommendations (replace with actual logic)
    num_recommendations = randint(1, 3)
    recommendations = [Product(name=generate_recommendation_name()) for _ in range(num_recommendations)]
    if isinstance(Product, BaseModel):
        return [Product(name=name) for name in recommendations]
    print(recommendations)
    return recommendations


# Endpoint for co-occurrence recommendations
@app.get("/products/{product_id}/coOccurrence")
async def get_cooccurrence_recommendations(product_id: int = Path(..., description="ID of the product")):
    # Simulate co-occurrence recommendations (replace with actual logic)
    num_recommendations = randint(2, 5)
    recommendations = [Product(name=generate_recommendation_name()) for _ in range(num_recommendations)]
    if isinstance(Product, BaseModel):
        return [Product(name=name) for name in recommendations]
    print(recommendations)
    return recommendations


# Run the FastAPI application (optional, for testing)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
