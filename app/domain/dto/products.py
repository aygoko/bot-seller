from domain.dto.base import DTO


class ProductDTO(DTO):
    """ DTO for class Product model """
    product_id: int
    product_name: str
    product_price: int
    product_type: str
    product_content: str
