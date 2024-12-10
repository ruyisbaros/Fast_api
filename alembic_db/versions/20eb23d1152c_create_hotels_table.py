"""create hotels table

Revision ID: 20eb23d1152c
Revises: 
Create Date: 2024-12-10 15:50:39.311498

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20eb23d1152c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'hotels',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(), index=True, nullable=False),
        sa.Column('address', sa.String(), nullable=False),
        sa.Column('city', sa.String(), index=True, nullable=False),
        sa.Column('stars', sa.Integer(), nullable=True),
        sa.Column('lowest_price', sa.Float(), index=True, nullable=True),
        sa.Column('accommodation', sa.String(), index=True, nullable=True),
        sa.Column('amenities', sa.ARRAY(sa.String()),
                  index=True, nullable=True),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('phone', sa.String(), nullable=True),
        sa.Column('photo_url', sa.ARRAY(sa.String()),
                  index=True, nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                  server_default=sa.text('now()'), nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table('hotels')  # noqa: E501  # pylint: disable=no-member,line-too-long
    pass
