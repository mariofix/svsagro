"""Customer access

Revision ID: 3bff85c8be56
Revises: d0886f658ce3
Create Date: 2022-11-18 21:23:34.686095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3bff85c8be56"
down_revision = "d0886f658ce3"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("svs_customer", schema=None) as batch_op:
        batch_op.add_column(sa.Column("key_uuid", sa.String(length=36), nullable=True))
        batch_op.add_column(sa.Column("key_pass", sa.String(length=6), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("svs_customer", schema=None) as batch_op:
        batch_op.drop_column("key_pass")
        batch_op.drop_column("key_uuid")

    # ### end Alembic commands ###