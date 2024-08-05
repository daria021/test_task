"""initial

Revision ID: 1866b84bbebd
Revises: 
Create Date: 2024-08-05 21:41:51.352632

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1866b84bbebd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('full_name', sa.String(length=100), nullable=False),
    sa.Column('birth_date', sa.Date(), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees')
    # ### end Alembic commands ###
