"""empty message

Revision ID: 9480148ef7c6
Revises: 0a37bcffad0f
Create Date: 2024-08-04 22:14:51.651250

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9480148ef7c6'
down_revision: Union[str, None] = '0a37bcffad0f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('modified_at', sa.DateTime(), nullable=True))
    op.add_column('replies', sa.Column('modified_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('replies', 'modified_at')
    op.drop_column('post', 'modified_at')
    # ### end Alembic commands ###
