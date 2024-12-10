"""create users table

Revision ID: 08dd890968e2
Revises: 20eb23d1152c
Create Date: 2024-12-10 16:16:15.416946

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08dd890968e2'
down_revision: Union[str, None] = '20eb23d1152c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('email', sa.String(), unique=True,
                  index=True, nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                  server_default=sa.text('now()'), nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table('users')  # noqa: E501  # pylint: disable=no-member,line-too-long
    pass
