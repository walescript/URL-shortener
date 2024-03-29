"""Qr code url column added to Link class

Revision ID: d7515a081954
Revises: 7db008aa4036
Create Date: 2023-06-18 17:36:52.668385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7515a081954'
down_revision = '7db008aa4036'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('link', schema=None) as batch_op:
        batch_op.add_column(sa.Column('qr_code_url', sa.String(length=512), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('link', schema=None) as batch_op:
        batch_op.drop_column('qr_code_url')

    # ### end Alembic commands ###
