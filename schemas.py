"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Padel products collection schema
    Collection name: "product" (lowercase of class name)
    """
    name: str = Field(..., description="Product name")
    brand: str = Field(..., description="Brand name")
    description: Optional[str] = Field(None, description="Product description")
    price_aed: float = Field(..., ge=0, description="Price in AED")
    category: str = Field("racket", description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")
    stock_qty: int = Field(10, ge=0, description="Quantity in stock")
    images: List[HttpUrl] = Field(default_factory=list, description="Image URLs")
    weight_grams: Optional[int] = Field(None, ge=300, le=400, description="Weight in grams")
    balance: Optional[str] = Field(None, description="Head-heavy, Even, or Head-light")
    surface: Optional[str] = Field(None, description="Carbon, Fiberglass, etc.")
    featured: bool = Field(False, description="Show as featured on homepage")

# Add your own schemas here:
# --------------------------------------------------

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
