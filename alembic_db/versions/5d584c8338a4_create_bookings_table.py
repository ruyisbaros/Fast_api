"""create bookings table

Revision ID: 5d584c8338a4
Revises: 08dd890968e2
Create Date: 2024-12-10 16:16:51.489486

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d584c8338a4'
down_revision: Union[str, None] = '08dd890968e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'bookings',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('hotel_id', sa.Integer(), nullable=False),
        sa.Column('customer_id', sa.String(), nullable=False),
        sa.Column('room_number', sa.Integer(), nullable=False),
        sa.Column('check_in', sa.Date(), nullable=False),
        sa.Column('check_out', sa.Date(), nullable=False),
        sa.Column('phone', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                  server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['hotel_id'], ['hotels.id']),
        sa.ForeignKeyConstraint(['customer_id'], ['users.id']),
        sa.UniqueConstraint('hotel_id', 'customer_id',
                            'room_number', 'check_in', 'check_out')

    )
    pass


def downgrade() -> None:
    op.drop_table('bookings')  # noqa: E501  # pylint: disable=no-member,line-too-long
    pass
