"""empty message

Revision ID: 2623ff35539c
Revises: d365b4864f1b
Create Date: 2024-06-30 20:37:21.202508

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '2623ff35539c'
down_revision: Union[str, None] = 'd365b4864f1b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'username',
               existing_type=mysql.VARCHAR(length=20),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('user', 'password',
               existing_type=mysql.VARCHAR(length=20),
               type_=sa.String(length=254),
               existing_nullable=False)
    op.alter_column('user', 'email',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=254),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'email',
               existing_type=sa.String(length=254),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=False)
    op.alter_column('user', 'password',
               existing_type=sa.String(length=254),
               type_=mysql.VARCHAR(length=20),
               existing_nullable=False)
    op.alter_column('user', 'username',
               existing_type=sa.String(length=50),
               type_=mysql.VARCHAR(length=20),
               existing_nullable=False)
    # ### end Alembic commands ###
