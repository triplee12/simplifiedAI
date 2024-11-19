"""empty message

Revision ID: b59d94316f39
Revises: 8108d1b32e2c
Create Date: 2024-11-19 14:11:49.730647

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'b59d94316f39'
down_revision: Union[str, None] = '8108d1b32e2c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chat', schema=None) as batch_op:
        batch_op.drop_column('title')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chat', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
